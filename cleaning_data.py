from imports import plt,LabelEncoder,msno,np

class DataCleaner:

    def __init__(self,df):
        self.df = df

    def replace_na(self):
        
        self.df = self.df.replace(['Not Applicable','Unknown'], np.nan)

        msno.bar(self.df)
        msno.heatmap(self.df)
        plt.show()


        self.df.drop(columns=['Number of Vehicles Registered at the Same Address'], errors='ignore', inplace=True)
        
        missing_row = self.df[self.df['Fuel Type'].isnull()]
        print(missing_row)
        
        self.df = self.df.drop('Region', axis=1)
        self.df = self.df.dropna(subset=['Fuel Type'])

        print('Unique Values', self.df['Vehicle Category'].unique())

    def categorical_to_numerical(self):
        label_encoder = LabelEncoder()

        self.df['Fuel Type'] = label_encoder.fit_transform(self.df['Fuel Type'])
        fuel_type_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
        print(f"Fuel Type Mapping: {fuel_type_mapping}")

        self.df['Vehicle Category'] = label_encoder.fit_transform(self.df['Vehicle Category'])
        vehicle_category_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
        print(f"Vehicle Mapping: {vehicle_category_mapping}")

        self.df['Fuel Technology'] = label_encoder.fit_transform(self.df['Fuel Technology'])
        fuel_technology_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
        print(f"Fuel Technology Mapping: {fuel_technology_mapping}")
        
        #df['Electric Mile Range'] = label_encoder.fit_transform(df['Electric Mile Range'])
        #Electric_mile_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
        #print(f"Fuel Technology Mapping: {Electric_mile_mapping}")


    def get_cleaned_data(self):
        self.replace_na()
        self.categorical_to_numerical()
        return self.df
    