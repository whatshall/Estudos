WITH cred AS (
	SELECT DATE_TRUNC('month', CAST(cred_date AS DATE)) AS dt_credenciamento,
	       accountid, 
		   COUNT(accountid) AS qtd_cred--ver accountid nulos 
	FROM dbadmin.tb_creds
	GROUP BY 1, 2
	),
	 cases AS (
	SELECT accountid, 
		   DATE_TRUNC('month', CAST(date_ref AS DATE)) AS dt_chamado, 
		   missed,
		   id
	FROM dbadmin.tb_cases
	WHERE TRUE 
	AND date_ref <> ''
	 ),
-------------------------
	 chamados AS (
	SELECT ca.dt_chamado,
	   	   COUNT(ca.missed) qtd_chamados,
	       cr.dt_credenciamento,
		   cr.qtd_cred
	FROM cases AS ca
	LEFT JOIN cred AS cr
		ON ca.accountid = cr.accountid
	GROUP BY 1, 3, 4
	ORDER BY 1 DESC),
-------------------------
	  mes_anterior AS (
	 SELECT dt_chamado,
		LAG(dt_chamado,1) OVER (
			ORDER BY dt_chamado
			) mes_anterior
	 FROM chamados
	 GROUP BY dt_chamado
	 ORDER BY dt_chamado DESC)
-------------------------
	SELECT CAST(c.dt_chamado AS DATE) AS dt_chamado, SUM(c.qtd_chamados), SUM(c.qtd_cred), CAST(c.dt_credenciamento AS DATE) AS dt_credenciamento, CAST(m.mes_anterior AS DATE) AS mes_anterior
	FROM chamados c
	LEFT JOIN mes_anterior m
		ON c.dt_chamado = m.dt_chamado
	WHERE TRUE
	AND c.dt_credenciamento = m.mes_anterior
	GROUP BY c.dt_chamado, c.dt_credenciamento, m.mes_anterior
	ORDER BY c.dt_chamado DESC, c.dt_credenciamento DESC

	
--UPDATE dbadmin.tb_creds SET cred_date = REPLACE(cred_date, '/','-')
--CREATE TABLE dbadmin.tb_creds
--(
--	id varchar(50),
--	cred_date varchar(50),
--	shipping_adress_city varchar(50),
--	shipping_adress_state varchar(50),
--	max_machine varchar(50),
--	accountid varchar(50)
--	);