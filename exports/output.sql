
DECLARE 
@start_date DATETIME = CONVERT(DATETIME,'2019-08-14 00:00:00'),
@end_date DATETIME = CONVERT(DATETIME,'2019-08-15 00:00:00')
;

DECLARE @Temp_Table TABLE(
    ID INT,
    technician NVARCHAR(255)
)
INSERT INTO @Temp_Table
SELECT
    nps.ID,
    replace(inc.resolvedby,'.',' ') as technician

FROM
    [LF-SQL-RPT01].[dbo].[lfliveextract_nps_reduction] NPS
    JOIN incidents_view_4 inc ON (inc.number = nps.incidentnumber AND inc.system = nps.system)
WHERE
    NPS.surveytype = 'incident'
    AND inc.lastmoddatetime BETWEEN @start_date AND @end_date;

/*MERGE THE TEMP TABLE WITH THE CLOSED INCIDENTS TABLE*/
MERGE [dbo].[lfliveextract_nps_reduction] target
Using @Temp_Table source
ON (
    target.ID = source.ID
)
WHEN MATCHED
THEN UPDATE
SET
target.technician = source.technician
WHEN NOT MATCHED BY TARGET
THEN INSERT 
(
technician
)
VALUES (
source.technician
);