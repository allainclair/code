# create a endpoint that receives a string and echoes it.

from fastapi import FastAPI
from sqlmodel import (
    Session,
    select)

from string import ascii_letters

import json

from string_model import StringModel

from dbapp import start as start_db

engine = start_db()
app = FastAPI()


@app.get("/{string}")
def read_root(string: str):
    # 'asdfgjl...a'
    # set = {1,2,3,}
    # 3 in set? O(1)

    with Session(engine) as session:
        statement = select(StringModel).where(StringModel.string == string)
        string_model = session.exec(statement).first()
        if string_model:
            return {"data": json.loads(string_model.object)}
        else:
            char_to_its_position = {}  # [[]]
            repeated_char_to_its_position = {}
            for position, char in enumerate(string):
                if char in char_to_its_position:  # O(N) complexity for nested lists
                    repeated_char_to_its_position[char] = char_to_its_position[char]
                else:
                    char_to_its_position[char] = position

            string_model = StringModel(string=string, object=json.dumps(
                repeated_char_to_its_position))
            session.add(string_model)
            session.commit()

    return {"data": repeated_char_to_its_position}
