class RBUser:
    def __init__(self,
                 user_id: int | None = None,
                 username: str | None = None
                 ):
        self.id = user_id
        self.username = username

    def to_dict(self) -> dict:
        data = {'id': self.id, 'username': self.username}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data