import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
  host="hostname",
  user="username",
  password="password",
  database="database"
)

cursor = conn.cursor()

# Execute SQL commands as shown in previous examples
cursor.execute("CREATE TABLE IF NOT EXISTS SkillsAssessment (...)")


CREATE TABLE SkillsAssessment (
    PlayerID INT PRIMARY KEY,
    TechnicalSkillsRating INT,
    PhysicalSkillsRating INT,
    TacticalSkillsRating INT,
    AssessmentDate DATE
);

INSERT INTO SkillsAssessment (PlayerID, TechnicalSkillsRating, PhysicalSkillsRating, TacticalSkillsRating, AssessmentDate)
VALUES (1, 8, 9, 7, '2024-05-01');

SELECT * FROM SkillsAssessment WHERE PlayerID = 1;

CREATE TABLE ProgressTracking (
    PlayerID INT,
    GoalID INT,
    ProgressPercentage INT,
    DateUpdated DATE,
    PRIMARY KEY (PlayerID, GoalID)
);

INSERT INTO ProgressTracking (PlayerID, GoalID, ProgressPercentage, DateUpdated)
VALUES (1, 101, 75, '2024-05-01');

SELECT * FROM ProgressTracking WHERE PlayerID = 1;

CREATE TABLE NutritionHealth (
    PlayerID INT PRIMARY KEY,
    DietaryRestrictions VARCHAR(255),
    HealthNotes VARCHAR(255)
);

INSERT INTO NutritionHealth (PlayerID, DietaryRestrictions, HealthNotes)
VALUES (1, 'No gluten', 'Allergy to nuts');

SELECT * FROM NutritionHealth WHERE PlayerID = 1;


CREATE TABLE PerformanceAnalytics (
    PlayerID INT,
    GameID INT,
    GoalsScored INT,
    AssistsMade INT,
    DistanceCovered FLOAT,
    GameDate DATE,
    PRIMARY KEY (PlayerID, GameID)
);

INSERT INTO PerformanceAnalytics (PlayerID, GameID, GoalsScored, AssistsMade, DistanceCovered, GameDate)
VALUES (1, 555, 2, 1, 10.5, '2024-05-01');

SELECT * FROM PerformanceAnalytics WHERE PlayerID = 1;
