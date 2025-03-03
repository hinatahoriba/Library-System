import asyncio
import websockets
from smartcard.System import readers
from smartcard.util import toHexString

# NFCリーダーを検索
r = readers()
if not r:
    print("NFCリーダーが見つかりません")
    exit(1)

reader = r[0]
print(f"使用するリーダー: {reader}")

# WebSocketハンドラー
async def nfc_handler(websocket, path):
    while True:
        message = await websocket.recv()
        if message == "read_nfc":
            try:
                # NFCリーダーに接続
                connection = reader.createConnection()
                connection.connect()

                # IDm (FeliCa) の取得
                POLLING = [0xFF, 0xCA, 0x00, 0x00, 0x00]
                data, sw1, sw2 = connection.transmit(POLLING)

                idm = toHexString(data[:8])
                pmm = toHexString(data[8:16])
                response = {"idm": idm, "pmm": pmm}

                # 取得したIDmをWebSocket経由で送信
                await websocket.send(str(response))
            except Exception as e:
                await websocket.send(f"Error: {str(e)}")

# WebSocketサーバーを起動 (ポート8765)
start_server = websockets.serve(nfc_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
