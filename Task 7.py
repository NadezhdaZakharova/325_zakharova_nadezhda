subst = "GK"
st = "gkgyugulolukilgkug"
def search_substr(subst, st):
    subst = subst.lower()
    st = st.lower()
    if subst in st:
        print ("«Есть контакт!»")
    else:
        print ("«Мимо!»")
    return
search_substr (subst, st)


