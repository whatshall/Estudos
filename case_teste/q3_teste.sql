SELECT DISTINCT 
		   dt_chamado,
		   month,
	       motivo, max_machine,
		   SUM(qtd_chamados) AS qtd_chamados
FROM dbadmin.vw_cluster
WHERE TRUE
--AND dt_chamado >= '2020-08-01'
GROUP BY 1, 2, 3, 4
ORDER BY 1 ASC
-------------------------