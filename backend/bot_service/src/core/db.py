from motor.motor_asyncio import AsyncIOMotorClient

from core.settings import (
    MONGO_URI,
    MONGO_DATABASE_NAME,
    MONGO_USER_NAME,
    MONGO_PASSWORD
)


async def init_db() -> None:
    """
        Init MongoDB and create user if doesnt exist.
        We retreive the users by Running usersInfo. This command will return the following:
        {
           "users" : [
              {
                 "_id" : "<db>.<username>",
                 "userId" : <UUID>,
                 "user" : "<username>",
                 "db" : "<db>",
                 "mechanisms" : [ ... ],
                 "customData" : <document>,
                 "roles" : [ ... ],
                 "credentials": { ... }, // only if showCredentials: true
                 "inheritedRoles" : [ ... ],  // only if showPrivileges: true or showAuthenticationRestrictions: true
                 "inheritedPrivileges" : [ ... ], // only if showPrivileges: true or showAuthenticationRestrictions:
                    trues
                 "inheritedAuthenticationRestrictions" : [ ] // only if showPrivileges: true or
                    showAuthenticationRestrictions: true
                 "authenticationRestrictions" : [ ... ] // only if showAuthenticationRestrictions: true
              },
              ...
           ],
           "ok" : 1
        }
        If doesnt exist, we create the user by running createUser command
    """
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[MONGO_DATABASE_NAME]

    response_users = await db.command("usersInfo")

    if not any(
        user.get("db") == MONGO_DATABASE_NAME
        and user.get("user") == MONGO_USER_NAME
        for user in response_users.get("users")
    ):
        await db.command(
            {
                "createUser": MONGO_USER_NAME,
                "pwd": MONGO_PASSWORD,
                "roles": [
                    {
                        "role": "readWrite",
                        "db": "chatbot_db"
                    }
                ]
            }
        )
