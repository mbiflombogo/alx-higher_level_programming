#!/usr/bin/python3
def search_replace(my_list, search, replace):
    m_dup = my_list[:]
    for i in range(len(m_dup)):
        if m_dup[i] == search:
            m_dup[i] = replace
    return m_dup
