
# autenticación
common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_API_KEY, {})

models = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")

# extraer clientes
clientes = models.execute_kw(
    ODOO_DB,
    uid,
    ODOO_API_KEY,
    'res.partner',
    'search_read',
    [[]],
    {'fields': ['name','email','phone']}
)

df = pd.DataFrame(clientes)

df.to_parquet("data/bronze/clientes.parquet")
