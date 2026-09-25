from supabase import create_client

SUPABASE_URL = "https://ggdxxbtonxxgfexmdsmf.supabase.co"
SUPABASE_KEY = "sb_publishable_1pCyabPlXRTOG9Jaf33q_A_G3qsVxDq"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Connected!")