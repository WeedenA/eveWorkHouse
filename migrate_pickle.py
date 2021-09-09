from PriceData import PriceData
from sqlalchemy import create_engine
from sqlalchemy.types import Date, Integer
import pandas as pd

HOST = '****'
USER = 'root'
PASS = '****'
DB = 'eve'

def main():
    engine = create_engine(f"mysql+pymysql://{USER}:{PASS}@{HOST}/{DB}"
                           )

    handler = PriceData()
    log = handler.openLog()

    df = pd.DataFrame(log)
    df.to_sql('ore_price_record', engine, if_exists='replace', index=False, index_label="date", dtype={"date": Date(), 'Loparite': Integer(), 'Monazite': Integer(),
                                                                                   'Xenotime': Integer(), 'Ytterbite': Integer(),
             'Carnotite': Integer(), 'Cinnabar': Integer(), 'Pollucite': Integer(), 'Zircon': Integer(),
             'Chromite': Integer(), 'Otavite': Integer(), 'Sperrylite': Integer(), 'Vanadinite': Integer() })
    #print(pd.read_sql_query("select * from ore_price_record", engine))
    #print(engine.execute("SELECT * FROM ore_price_record").fetchall())


if __name__ == "__main__":
    main()