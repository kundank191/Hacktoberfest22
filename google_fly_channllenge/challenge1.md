# Task 1

- open the consolse
- `gsutil ls "gs://bucket/foldername/*.csv"`
- ```py
    bq mk drl
    for file in `gsutil ls gs://spls/gsp394/tables/*.csv`; do TABLE_NAME=`echo $file | cut -d '/' -f6 | cut -d '.' -f1`; bq load --autodetect --source_format=CSV --replace=true drl.$TABLE_NAME $file; done
````
- ``` sql
    create schema `investing-302614`.abcd;
    LOAD DATA OVERWRITE drl.colors
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/colors.csv']);
    

    LOAD DATA OVERWRITE drl.event_crossings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/event_crossings.csv']);
    

    LOAD DATA OVERWRITE drl.event_pilots
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/event_pilots.csv']);
    

    LOAD DATA OVERWRITE drl.event_standings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/event_standings.csv']);
    

    LOAD DATA OVERWRITE drl.events
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/events.csv']);
    

    LOAD DATA OVERWRITE drl.heat_pilot_crossings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/heat_pilot_crossings.csv']);
    

    LOAD DATA OVERWRITE drl.heat_pilots
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/heat_pilots.csv']);
    

    LOAD DATA OVERWRITE drl.heat_standings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/heat_standings.csv']);
    

    LOAD DATA OVERWRITE drl.heats
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/heats.csv']);
    

    LOAD DATA OVERWRITE drl.pilot_asset_playlists
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/pilot_asset_playlists.csv']);
    

    LOAD DATA OVERWRITE drl.pilot_assets
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/pilot_assets.csv']);
    

    LOAD DATA OVERWRITE drl.pilot_season_stats
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/pilot_season_stats.csv']);
    

    LOAD DATA OVERWRITE drl.pilots
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/pilots.csv']);
    

    LOAD DATA OVERWRITE drl.race_standings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/race_standings.csv']);
    

    LOAD DATA OVERWRITE drl.races
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/races.csv']);
    

    LOAD DATA OVERWRITE drl.round_standings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/round_standings.csv']);
    

    LOAD DATA OVERWRITE drl.rounds
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/rounds.csv']);
    

    LOAD DATA OVERWRITE drl.scorings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/scorings.csv']);
    

    LOAD DATA OVERWRITE drl.seasons
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/seasons.csv']);
    

    LOAD DATA OVERWRITE drl.time_trial_group_pilot_crossings
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/time_trial_group_pilot_crossings.csv']);
    

    LOAD DATA OVERWRITE drl.time_trial_group_pilot_times
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/time_trial_group_pilot_times.csv']);
    

    LOAD DATA OVERWRITE drl.time_trial_group_pilots
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/time_trial_group_pilots.csv']);
    

    LOAD DATA OVERWRITE drl.time_trial_groups
    FROM FILES (
    format = 'CSV',
    uris = ['gs://spls/gsp394/tables/time_trial_groups.csv']); 
    ```
- ``` sql
    create or replace table drl.colors as
    select
    *
    from drl.colors ;


    create or replace table drl.event_crossings as
    select
    *
    from drl.event_crossings ;


    create or replace table drl.event_pilots as
    select
    *
    from drl.event_pilots ;


    create or replace table drl.event_standings as
    select
    *
    from drl.event_standings ;


    create or replace table drl.events as
    select
    *
    from drl.events ;


    create or replace table drl.heat_pilot_crossings as
    select
    *
    from drl.heat_pilot_crossings ;


    create or replace table drl.heat_pilots as
    select
    *
    from drl.heat_pilots ;


    create or replace table drl.heat_standings as
    select
    *
    from drl.heat_standings ;


    create or replace table drl.heats as
    select
    *
    from drl.heats ;


    create or replace table drl.pilot_asset_playlists as
    select
    *
    from drl.pilot_asset_playlists ;


    create or replace table drl.pilot_assets as
    select
    *
    from drl.pilot_assets ;


    create or replace table drl.pilot_season_stats as
    select
    *
    from drl.pilot_season_stats ;


    create or replace table drl.pilots as
    select
    *
    from drl.pilots ;


    create or replace table drl.race_standings as
    select
    *
    from drl.race_standings ;


    create or replace table drl.races as
    select
    *
    from drl.races ;


    create or replace table drl.round_standings as
    select
    *
    from drl.round_standings ;


    create or replace table drl.rounds as
    select
    *
    from drl.rounds ;


    create or replace table drl.scorings as
    select
    *
    from drl.scorings ;


    create or replace table drl.seasons as
    select
    *
    from drl.seasons ;


    create or replace table drl.time_trial_group_pilot_crossings as
    select
    *
    from drl.time_trial_group_pilot_crossings ;


    create or replace table drl.time_trial_group_pilot_times as
    select
    *
    from drl.time_trial_group_pilot_times ;


    create or replace table drl.time_trial_group_pilots as
    select
    *
    from drl.time_trial_group_pilots ;


    create or replace table drl.time_trial_groups as
    select
    *
    from drl.time_trial_groups ;
```

# Task 2

``` sql
select
distinct
name
from `drl.events`
where city = 'Memphis'
```

# Task 3

``` sql
select
distinct
b.name as name,
a.id as event_pilot_id
from `drl.event_pilots` a
left join `drl.pilots` b on a.pilot_id = b.id
```

# Task 4
``` sql
select
distinct
b.name as pilot_name,
c.name as event_name
from `drl.event_pilots` a
left join `drl.pilots` b on a.pilot_id = b.id
inner join `drl.events` c on a.event_id = c.id and c.name = 'California Nights'
```

# Task 5
``` sql
SELECT time
 (timestamp_seconds
   (CAST
     (AVG
       (UNIX_SECONDS
         (PARSE_TIMESTAMP('%H:%M.%S', minimum_time))
       )
   AS INT64)
   )
 ) as avg
from `drl.round_standings`
where rank = 1
```

# Task 6

``` sql
create table drl.time_trial_cleaned as
select
a.id as time_trial_group_pilot_times_id,
a.time_trial_group_pilot_id,
b.time_trial_group_id,
c.round_id,
case 
when a.time_adjusted is not null then a.time_adjusted
when c.racestack_scoring = 0 then a.time
else a.racestack_time end as time
from drl.time_trial_group_pilot_times a
left join drl.time_trial_groups c on a.time_trial_group_pilot_id = c.id
left join drl.time_trial_group_pilots b on c.id = b.time_trial_group_id
```

# Task 7

``` sql
select
min(c.time) as fastest_time
from `drl.events` a
left join `drl.rounds` b on b.event_id = a.id
left join drl.time_trial_cleaned c on b.id = c.round_id
where a.name = 'California Nights'
and b.name = 'Time Trials'
```

# Task 8

``` sql
select
distinct
c.name as pilot_name,
a.heat_id,
a.minimum_time,
a.points
from `drl.heat_standings` a
left join `drl.event_pilots` b on a.event_pilot_id = b.id
left join `drl.pilots` c on b.pilot_id = c.id
where a.minimum_time <> ""
and a.minimum_time <> 'DNF'
and c.name = 'GAB707'
```

# Task 9

``` sql
select
distinct
c.name as pilot_name,
a.heat_id,
a.minimum_time,
a.points,
  time 
    (timestamp_seconds
      (CAST
        (AVG
          (UNIX_SECONDS
            (PARSE_TIMESTAMP('%H:%M.%S', a.minimum_time))
          )
        OVER (ORDER BY a.heat_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
      AS INT64)
      )
    )
  AS running_avg
from `drl.heat_standings` a
left join `drl.event_pilots` b on a.event_pilot_id = b.id
left join `drl.pilots` c on b.pilot_id = c.id
where a.minimum_time <> ""
and a.minimum_time <> 'DNF'
and c.name = 'GAB707'
```

# Task 10

``` SQL
select
pilot_name,
heat_id,
minimum_time,
points,
running_avg,
TIME_DIFF(PARSE_TIME('%H:%M.%S', minimum_time), running_avg, SECOND) as time_diff_from_avg
from (
  select
  distinct
  c.name as pilot_name,
  a.heat_id,
  a.minimum_time,
  a.points,
    time 
      (timestamp_seconds
        (CAST
          (AVG
            (UNIX_SECONDS
              (PARSE_TIMESTAMP('%H:%M.%S', a.minimum_time))
            )
          OVER (ORDER BY a.heat_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
        AS INT64)
        )
      )
    AS running_avg
  from `drl.heat_standings` a
  left join `drl.event_pilots` b on a.event_pilot_id = b.id
  left join `drl.pilots` c on b.pilot_id = c.id
  where a.minimum_time <> ""
  and a.minimum_time <> 'DNF'
  and c.name = 'NURK'
)
```

# Task 11
``` SQL
select 
c.name as name, 
a.minimum_time as minimum_time, 
a.heat_id as heat_id, 
safe_cast(a.points as integer) as points 
from drl.heat_standings a 
join drl.event_pilots b on a.event_pilot_id = b.id 
join drl.pilots c on b.pilot_id = c.id 
 
where minimum_time not in ( "DNF" , "0") 
and points != 0
order by heat_id asc
```

