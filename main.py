from autobahn.twisted.wamp import ApplicationSession


class MainSession(ApplicationSession):
    async def onJoin(self, details):
        print("joined session", details)
        await self.register(self.add2, "pk.codebase.wamp.add2")

    async def add2(self, num1, num2):
        return num1 + num2


