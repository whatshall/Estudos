WITH cred AS (
	SELECT cred_date AS dt_credenciamento, 
	   shipping_adress_city, 
	   shipping_adress_state, 
	   max_machine, 
	   accountid
	FROM dbadmin.tb_creds
	),
	 cases AS (
	SELECT accountid, 
		   date_ref, 
		   channelid, 
		   waitingtime, 
		   missed, 
		   pesquisa_de_satisfa_o__c, 
		   assunto, 
		   id
	FROM dbadmin.tb_cases
	WHERE TRUE 
	AND date_ref IS NOT NULL)
-------------------------
SELECT --date_ref, 
	   assunto, 
	   --shipping_adress_state, max_machine,
	   COUNT(DISTINCT ca.accountid) AS cont
FROM cases AS ca
LEFT JOIN cred AS cr
	ON ca.accountid = cr.accountid
GROUP BY --date_ref, 
		 assunto
ORDER BY cont DESC