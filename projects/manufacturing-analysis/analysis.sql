-- Synthetic Manufacturing Analytics

SELECT Machine,
       SUM(Production_Target) AS target_units,
       SUM(Units_Produced) AS produced_units,
       ROUND(100.0 * SUM(Units_Produced) / SUM(Production_Target), 2) AS achievement_pct,
       SUM(Defects) AS defects,
       ROUND(100.0 * SUM(Defects) / SUM(Units_Produced), 2) AS defect_rate_pct,
       SUM(Downtime_Minutes) AS downtime_minutes
FROM manufacturing
GROUP BY Machine
ORDER BY achievement_pct DESC;
