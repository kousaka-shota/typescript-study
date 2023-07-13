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
def add_equipment(db:Session,equipment:schemas.Equipment):
    #API側から取得している登録したい情報をインスタンスを生成時の引数として渡す。id等の自動登録されるものは渡さない
    db_equipment = models.Equipment(equip_name=equipment.equip_name,equip_asset_No=equipment.equip_asset_No)

    #dbへ仮保存。複数データを登録する場合はaddをたくさんしてからまとめて一回でcomitする
    db.add(db_equipment)
    db.commit()

    #commitでdb側に反映されるがセッション情報をリセットし新しい情報を入れるために必要
    db.refresh(db_equipment)
    return db_equipment
    
#センサ―の追加

#データの追加

#設備情報の編集

#センサ―情報の編集

#設備の削除

#センサ―の削除


