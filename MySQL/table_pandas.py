import pandas as pd

from faker import Faker

from collections import defaultdict 

from sqlalchemy import create_engine

fake = Faker()

data_dump = defaultdict(list)

for _ in range(10):
    data_dump["id"].append(_)
    data_dump["first_name"].append( fake.first_name() )
    data_dump["last_name"].append( fake.last_name() )
    data_dump["name"].append(fake.name())
    data_dump["occupation"].append( fake.job() )
    data_dump["dob"].append( fake.date_of_birth() )
    data_dump["country"].append( fake.country() )
    data_dump["address"].append( fake.address())
    data_dump["state"].append(fake.state())
    data_dump["city"].append(fake.city())
    data_dump["number"].append(fake.phone_number())
    data_dump["important_date"].append( fake.date_of_birth() )
    data_dump["credit_card_number"].append(fake.credit_card_number())
    data_dump["credit_card_expiry_date"].append(fake.credit_card_expire())
    data_dump["credit_card"].append(fake.credit_card_full())
    data_dump["email"].append(fake.email())
    data_dump["URL"].append(fake.url())
    data_dump["license_plate"].append(fake.license_plate())
    data_dump["currency_code"].append(fake.currency_code())
    data_dump["currency_full_form"].append(fake.currency())
    data_dump["currency"].append(fake.currency())
    data_dump["colour_name"].append(fake.color_name())
    data_dump["local_latlng"].append(fake.local_latlng())
    data_dump["local_latitude"].append(fake.latitude())
    data_dump["local_longitude"].append(fake.longitude())
    data_dump["area"].append(fake.license_plate())
    data_dump["text"].append(fake.text())
    data_dump["domain_name"].append(fake.domain_name())
    data_dump["text"].append(fake.text())
    data_dump["company"].append(fake.company())
    
    

df_data_dump = pd.DataFrame(data_dump)

# engine = create_engine('mysql://root:passwod@127.0.0.1/Demo', echo=False)
# engine = create_engine('mysql+mysqldb://root:password@locahost/Demo', echo=False)
engine = create_engine('mysql+mysqldb://root:password@127.0.0.1/Demo', echo=False)

df_data_dump.to_sql('Dummy', con=engine, index=False)