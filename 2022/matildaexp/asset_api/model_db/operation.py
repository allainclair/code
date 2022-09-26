from sqlmodel import (
    Session,
    select)


def delete_by_id(engine, model_class, id_):
    with Session(engine) as session:
        model_instance = select_first_by_id(engine, model_class, id_)
        if model_instance:
            session.delete(model_instance)
            session.commit()
            return model_class(**dict(model_instance))
    return False


def save_and_refresh(engine, model_instance):
    with Session(engine) as session:
        session.add(model_instance)
        session.commit()
        session.refresh(model_instance)
        return True


def select_all(engine, model_class):
    with Session(engine) as session:
        statement = select(model_class)
        return session.exec(statement).all()


def select_first_by_id(engine, model_class, id_):
    with Session(engine) as session:
        statement = select(model_class).where(model_class.id == id_)
        return session.exec(statement).first()


def update_and_refresh_by_id(engine, model_class, id_, updating_model):
    with Session(engine) as session:
        model_instance = select_first_by_id(engine, model_class, id_)
        if model_instance:
            model_instance = _update_model(model_instance, updating_model)
            session.add(model_instance)
            session.commit()
            session.refresh(model_instance)
            return model_class(**dict(model_instance))
    return False


def _update_model(model_to_update, new_model):
    del new_model.id  # Avoid database unique id exception.
    for attr, value in dict(new_model).items():
        if not attr.startswith('_'):  # Avoid to overwrite private attributes.
            setattr(model_to_update, attr, value)
    return model_to_update
