const { Pool, Client } = require("pg") 
const connectionString = 'postgresql://root:GNOAKKAdvf0NlVU.0S1B1fYY2G.Kvvad@10.243.56.70:3306/composer-1-19-8-airflow-2-2-5-34e4e28b'
const fs = require("fs");
csv = require("csv-stringify");


async function main(){
const pool = new Pool({
  connectionString,
})
sql_query = `SELECT 
dr.id,
dr.dag_id, 
ROUND(EXTRACT(EPOCH FROM (dr.end_date - dr.start_date))/60) duration,
'' rong,
dr.state,
TO_CHAR(dr.start_date at time zone 'Asia/Ho_Chi_Minh','YYYY-MM-DD HH24:MI:SS') start_datetime,
TO_CHAR(dr.start_date at time zone 'Asia/Ho_Chi_Minh','YYYY-MM-DD') start_date

FROM dag d
LEFT JOIN dag_run dr on dr.dag_id = d.dag_id
WHERE d.is_paused <> true AND d.is_active = true
AND d.dag_id <> 'vhm_sf_afs_leadscoring_prod'
AND d.dag_id <> 'vhm_sf_afs_leadscoring_dev'
AND d.dag_id <> 'airflow_monitoring'
AND dr.start_date > '2023-12-10 16:00:00'
AND dr.start_date < '2023-12-31 16:00:00'
ORDER BY dr.dag_id ASC
`
// WHERE dag_id = 'vhm_etl_data_from_fbads_to_datalake_prod'

var a = await pool.query(sql_query)
await pool.end()
console.log(a.rowCount)
// console.log(a.rows)

var dataToWrite = a.rows
//console.log(dataToWrite)
csv.stringify(dataToWrite, {
  header : true,
//   columns : { ani : "Animal", desc : "Description" }
}, (err, output) => {
  fs.writeFileSync("data.csv", output);
  console.log("OK");
});
    
// const client = new Client({
//   connectionString,
// })
 
// await client.connect()
 
// await client.query('SELECT NOW()')
 
// await client.end()
}
main()

