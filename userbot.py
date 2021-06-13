api_id = 4538322
api_hash = 891868e1bfc6f96a1ac7f8208a5cf5c4
string_session = AQA1bnTlcPGaALjN1-mKv_oBrtOQmc2yArcKaVw984vKHiLDGeA8_PlTizreSnb_19mY3RhsAkDKBEan8gyfcW4njw3me_tpk-2lGRKgfDf-4-1HeYqZ9fnUdxARBpvjZH2xWus3-iM_i75dQbfNb8HhRyETRfSIOKDsl77aE0BxoHpwLMehiRXbQtUSc13vOzx1D7G3L1z05ejkdztPfqbrMzxnQ1YENg4rjuJeSDUQao3YwxCZ4SfFdBZmILf68b5D8BhmE04rLyOXA7UVpoTLK14BOJnwKeJIY594BYC8tJTED-FsW6jiaqvJ2nSpkl_D5y76E1F7M7nRVn0St1zgaLNC0gA
plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
