CREATE VIEW dbadmin.vw_cluster AS
WITH 
cases AS (
	SELECT DISTINCT 
		   CAST(date_ref AS DATE) AS dt_chamado,--DATE_TRUNC('month', CAST(date_ref AS DATE)) AS dt_chamado, 
		   CASE 
			WHEN assunto LIKE ('Logística%') THEN 'Logística' 
			WHEN assunto LIKE ('Produto%') THEN 'Produto' 
			WHEN assunto LIKE ('Aplicativo%') THEN 'Aplicativo' 
			WHEN assunto LIKE ('Pedido%') THEN 'Pedido' 
			WHEN assunto LIKE ('Incidente%') THEN 'Incidente' 
			WHEN assunto LIKE ('Cadastro%') THEN 'Cadastro' 
			WHEN assunto LIKE ('Transação%') THEN 'Transação'
			WHEN assunto LIKE ('Outros%') THEN 'Outros'
			ELSE 'Outros'
	   	   END AS motivo,
		   COUNT(accountid) AS qtd,
		   accountid
	FROM dbadmin.tb_cases
	WHERE TRUE 
	AND date_ref <> ''
	GROUP BY 1, 2, 4
	ORDER BY 1 DESC),
creds AS (
	SELECT DISTINCT 
		   cred_date, 	
		   max_machine, 
		   accountid
	FROM dbadmin.tb_creds)
-------------------------
SELECT CAST(ca.dt_chamado AS DATE) AS dt_chamado,
	   TO_CHAR(ca.dt_chamado, 'Month') AS "month", 
	   motivo,
	   cr.max_machine, 
	   SUM(qtd) AS qtd_chamados
FROM cases AS ca
LEFT JOIN creds as cr
	ON ca.accountid = cr.accountid
WHERE TRUE
AND max_machine <> 'NONE'
GROUP BY ca.dt_chamado, 
         motivo, 
	     cr.max_machine
ORDER BY ca.dt_chamado ASC