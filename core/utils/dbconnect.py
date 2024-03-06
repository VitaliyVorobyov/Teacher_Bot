import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def create_table(self):

        create_users = (f"CREATE TABLE IF NOT EXISTS Users ("
                        f"id SERIAL PRIMARY KEY,"
                        f"user_id INTEGER UNIQUE NOT NULL)")

        create_buttons = (f"CREATE TABLE IF NOT EXISTS Buttons ("
                          f"button_id SERIAL PRIMARY KEY,"
                          f"name_button VARCHAR(100) UNIQUE NOT NULL,"
                          f"start_button BOOLEAN DEFAULT FALSE NOT NULL)")

        crete_file = (f"CREATE TABLE IF NOT EXISTS Files ("
                      f"row_id SERIAL PRIMARY KEY,"
                      f"file_id VARCHAR(100) NOT NULL)")

        crete_description = (f"CREATE TABLE IF NOT EXISTS Description ("
                             f"description_id SERIAL PRIMARY KEY,"
                             f"description VARCHAR(100) NOT NULL)")

        create_file_to_description = (f"CREATE TABLE IF NOT EXISTS File_To_Description ("
                                      f"file_to_description_id SERIAL PRIMARY KEY,"
                                      f"row_id INTEGER REFERENCES Files(row_id) "
                                      f"ON DELETE CASCADE ON UPDATE CASCADE,"
                                      f"description_id INTEGER REFERENCES Description(description_id))")

        create_buttons_to_button = (f"CREATE TABLE IF NOT EXISTS Buttons_To_Button ("
                                    f"buttons_to_button_id SERIAL PRIMARY KEY,"
                                    f"button_id INTEGER REFERENCES Buttons(button_id) "
                                    f"ON DELETE CASCADE ON UPDATE CASCADE,"
                                    f"button_id_to INTEGER REFERENCES Buttons(button_id) "
                                    f"ON DELETE CASCADE ON UPDATE CASCADE)")

        crete_content_to_button = (f"CREATE TABLE IF NOT EXISTS Content_To_Button ("
                                   f"content_to_button_id SERIAL PRIMARY KEY,"
                                   f"button_id INTEGER REFERENCES Buttons(button_id) "
                                   f"ON DELETE CASCADE ON UPDATE CASCADE,"
                                   f"file_to_description_id INTEGER REFERENCES "
                                   f"File_To_Description(file_to_description_id)"
                                   f"ON DELETE CASCADE ON UPDATE CASCADE)")

        await self.connector.execute(create_users)
        await self.connector.execute(create_buttons)
        await self.connector.execute(create_buttons_to_button)
        await self.connector.execute(crete_file)
        await self.connector.execute(crete_description)
        await self.connector.execute(create_file_to_description)
        await self.connector.execute(crete_content_to_button)

    async def add_button(self, name: str):
        return await self.connector.fetchval(
            "INSERT INTO Buttons(name_button) VALUES($1) RETURNING button_id",
            name
        )

    async def add_button_start(self, name: str):
        await self.connector.execute(
            "INSERT INTO Buttons(name_button, start_button) VALUES($1, $2)",
            name, True
        )

    async def add_new_button_to_button(self, button_id: int, button_id_to: int):
        await self.connector.execute(
            "INSERT INTO Buttons_To_Button(button_id, button_id_to) VALUES($1, $2)",
            button_id, button_id_to
        )

    async def get_buttons(self):
        return await self.connector.fetch("SELECT * FROM Buttons")

    async def get_buttons_for_menu(self, button_id: int):
        return await self.connector.fetch(
            "SELECT button_id_to, name_button FROM Buttons_To_Button INNER JOIN Buttons "
            "ON Buttons.button_id = Buttons_To_Button.button_id_to WHERE buttons_to_button.button_id = $1",
            button_id
        )

    async def add_file_id(self, file_id: str):
        return await self.connector.fetchval(
            "INSERT INTO Files(file_id) VALUES($1) RETURNING row_id",
            file_id
        )

    async def add_description(self, description: str):
        return await self.connector.fetchval(
            "INSERT INTO Description(description) VALUES($1) RETURNING description_id",
            description
        )

    async def add_file_to_description(self, row_id: int, description_id: int):
        return await self.connector.fetchval(
            "INSERT INTO File_To_Description(row_id, description_id) VALUES($1, $2) RETURNING file_to_description_id",
            row_id, description_id
        )

    async def add_content_to_button(self, button_id: int, file_to_description_id: int):
        await self.connector.execute(
            "INSERT INTO Content_To_Button(button_id, file_to_description_id) VALUES($1, $2)",
            button_id, file_to_description_id
        )

    async def get_content_for_button(self, button_id: int):
        return await self.connector.fetch(
            "SELECT file_to_description_id FROM Content_To_Button WHERE button_id = $1",
            button_id
        )

    async def get_file_to_description(self, file_to_description_id: int):
        return await self.connector.fetch(
            "SELECT description_id, row_id FROM File_To_Description WHERE file_to_description_id = $1",
            file_to_description_id
        )

    async def get_description(self, description_id: int):
        return await self.connector.fetchval(
            "SELECT description FROM Description WHERE description_id = $1",
            description_id
        )

    async def get_file(self, row_id: int):
        return await self.connector.fetchval(
            "SELECT file_id FROM Files WHERE row_id = $1",
            row_id
        )

    async def add_user(self, user_id: int):
        return await self.connector.fetchval(
            "INSERT INTO Users(user_id) VALUES($1)",
            user_id
        )

    async def get_users(self):
        return await self.connector.fetch(
            "SELECT user_id FROM Users"
        )

    async def delete_button(self, button_id: int):
        await self.connector.execute(
            "DELETE FROM Buttons WHERE button_id = $1",
            button_id
        )

    async def delete_content_to_button(self, button_id: int):
        await self.connector.execute(
            "DELETE FROM Content_To_Button WHERE button_id = $1",
            button_id
        )