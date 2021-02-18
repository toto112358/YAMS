# -*- coding: utf-8 -*-
print("""YAMS_TCP_SENDER(1)          General Commands Manual         YAMS_TCP_SENDER(1)



tcp.sender — message sending module of the YAMS messaging system

stdin (message) --> tcp.sender HOST:PORT
tcp.sender will take its input from the stdin, and forward its input
to its arguments HOST:PORT.


CClliieenntt ssiiddee
       sh-5.1$ echo 'luca This is a msg from Luca'| yams msg_processor | yams tcp.sender localhost:1234
       Sent: luca 231491187591521828709693806234833716049963092
       Received: OK
       _N_o_t_e  _t_h_a_t  _m_s_g___p_r_o_c_e_s_s_o_r _E_N_C_R_Y_P_T_S _t_h_e _m_e_s_s_a_g_e _u_s_i_n_g _a _s_p_e_c_i_f_i_e_d _m_o_d_u_l_e
       _(_h_e_r_e_, _e_n_c_o_d_e_)_.

SSeerrvveerr ssiiddee
       sh-5.1$ yams tcp.server localhost:1234
       luca wrote 231491187591521828709693806234833716049963092


       L. Pham-Trong, S. Vallette


       tcp.sender, encode, decode, encrypt.twofish, decrypt.twofish



                                                            YAMS_TCP_SENDER(1)
""")
