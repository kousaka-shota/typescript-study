from sqlalchemy.orm import Session
from . import models,schemas

#設備一覧取得
def get_equipments(db:Session):
    return db.query(models.Equipment).all()

#センサー一覧取得
def get_sensors(db:Session):
    return db.query(models.Sensor).all()

#全計測データ取得

#計測データをフィルターして取得（期間・設備・センサ―）

#設備の追加

#センサ―の追加

#データの追加

#設備情報の編集

#センサ―情報の編集

#設備の削除

#センサ―の削除


