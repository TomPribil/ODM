CREATE TABLE Time_Dimension (
    Time_ID INT AUTO_INCREMENT,
    Harvest_Year YEAR(4),
    Grading_Date DATE,
    Expiration DATE,
    PRIMARY KEY (Time_ID)
);

CREATE TABLE Harvest_Information (
    Harvest_ID INT AUTO_INCREMENT,
    Time_ID INT,
    Lot_Number VARCHAR(255),
    FOREIGN KEY (Time_ID) REFERENCES Time_Dimension(Time_ID),
    PRIMARY KEY (Harvest_ID)
);

CREATE TABLE Farm (
    Farm_ID INT AUTO_INCREMENT,
    Farm_Name VARCHAR(255),
    Altitude VARCHAR(255),
    Producer VARCHAR(255),
    Country_of_Origin VARCHAR(255),
    Region VARCHAR(255),
    PRIMARY KEY (Farm_ID)
);

CREATE TABLE Coffee_Characteristics (
    Characteristics_ID INT AUTO_INCREMENT,
    Variety VARCHAR(255),
    Processing_Method VARCHAR(255),
    Color VARCHAR(255),
    PRIMARY KEY (Characteristics_ID)
);

CREATE TABLE Company (
    Company_ID INT AUTO_INCREMENT,
    Company VARCHAR(255),
    In_Country_Partner VARCHAR(255),
    Certification_Body VARCHAR(255),
    Certification_Address VARCHAR(255),
    Certification_Contact VARCHAR(255),
    PRIMARY KEY (Company_ID)
);

CREATE TABLE Bagging (
    Bag_ID INT AUTO_INCREMENT,
    Number_of_Bags INT,
    Bag_Weight VARCHAR(255),
    PRIMARY KEY (Bag_ID)
);

CREATE TABLE Defects (
    Defect_ID INT AUTO_INCREMENT,
    Category_One_Defects INT,
    Quakers INT,
    Category_Two_Defects INT,
    PRIMARY KEY (Defect_ID)
);

CREATE TABLE Coffee_Ratings (
    ID INT AUTO_INCREMENT,
    Farm_ID INT,
    Characteristics_ID INT,
    Harvest_ID INT,
    Company_ID INT,
    Bag_ID INT,
    Defect_ID INT,
    Total_Cup_Points DECIMAL(5,2),
    Aroma DECIMAL(5,2),
    Flavor DECIMAL(5,2),
    Aftertaste DECIMAL(5,2),
    Acidity DECIMAL(5,2),
    Body DECIMAL(5,2),
    Balance DECIMAL(5,2),
    Uniformity DECIMAL(5,2),
    Clean_Cup DECIMAL(5,2),
    Sweetness DECIMAL(5,2),
    Overall DECIMAL(5,2),
    Defects DECIMAL(5,2),
    Moisture_Percentage DECIMAL(5,2),
    PRIMARY KEY (ID),
    FOREIGN KEY (Farm_ID) REFERENCES Farm(Farm_ID),
    FOREIGN KEY (Characteristics_ID) REFERENCES Coffee_Characteristics(Characteristics_ID),
    FOREIGN KEY (Harvest_ID) REFERENCES Harvest_Information(Harvest_ID),
    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID),
    FOREIGN KEY (Bag_ID) REFERENCES Bagging(Bag_ID),
    FOREIGN KEY (Defect_ID) REFERENCES Defects(Defect_ID)
);
