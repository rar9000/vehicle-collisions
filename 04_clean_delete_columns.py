import pandas as pd

df1 = pd.read_csv('data/raw_data/raw_merge/raw_data_main.csv')
df2 = pd.read_csv('data/raw_data/raw_merge/raw_data_car.csv')

# remove unnecessary columns from both dataframes
df1 = df1.drop(
    ['AgencyORI','AgencyName','Street','County','IncidentStatusDesc','RdwyNumber','StreetDir','StreetSfx',
     'IntersectionRdwy','BetweenStRdwy1','BetweenStRdwyName1','BetweenStRdwy2','BetweenStRdwyName2',
     'Latitude','Longitude','Milepoint','UnitsInvolved','RdwyCharacter','RampFromRdwyId','RampToRdwyId',
     'AcceptedDate','AcceptedDate','OwnerBadge','IsSecondaryCollision','IncidentStatus'], axis=1,
    )

df2 = df2.drop(
    ['UnitNumber','UnitType','AirbagSwitchCde','IsCommercialVeh','CrashAvoidCde','DriverIdentifiedCde',
     'EventCollWithFirstCde','EventCollWithSecondCde','HasFire','PreCollActionCde','UnderOverrideCde',
     'VehicleIsInsured','MakeCde','ModelCde','VehicleType'], axis=1,
    )

# naming index for main data as this is last cleaning step for main
df1.index.name = 'Index'
df1.to_csv("data/clean_data/clean_data_main.csv") # allowing index and putting in clean directory
df2.to_csv("data/raw_data/raw_merge/raw_data_car.csv", index=False)
     
