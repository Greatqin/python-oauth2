from oauth2 import Provider
from oauth2.tokengenerator import Uuid4
from oauth2.store.memory import ClientStore, TokenStore
from oauth2.web.tornado import OAuth2Handler
from tornado.ioloop import IOLoop
from tornado.web import Application, url

client_store = ClientStore()
token_store = TokenStore()

provider = Provider(access_token_store=token_store,
                    auth_code_store=token_store, client_store=client_store,
                    token_generator=Uuid4())

app = Application([
    url(provider.authorize_path, OAuth2Handler, dict(provider=provider)),
    url(provider.token_path, OAuth2Handler, dict(provider=provider)),
])

app.listen(8888)
IOLoop.current().start()