import os
# 优选域名
domains=[
    'skk.moe',
    'visa.com',
    'visa.co.jp',
    'visa.com.sg',
    'visakorea.com',
    'cip.951535.xyz',
    'acjp2.cloudflarest.link',
]
# Cloudflare Port
port_tuple_01 = ('443', '2053', '2083', '2087', '2096', '8443')
port_tuple_02 = ('80', '8080', '8880', '2052', '2082', '2086', '2095')

# 待解析节点
dict={
    'godlike_vl':'vless://323f5607-f006-4de1-ad9f-979ebcad7ccf@government.se:443?security=tls&sni=godlike_tunnel.hengda.cloudns.biz&type=ws&path=/vless?ed%3D2048&host=godlike_tunnel.hengda.cloudns.biz&encryption=none#05-godlike_tunnel-ua-vl',
    'godlike_tr':'trojan://323f5607-f006-4de1-ad9f-979ebcad7ccf@government.se:443?security=tls&sni=godlike_tunnel.hengda.cloudns.biz&type=ws&path=/trojan?ed%3D2048&host=godlike_tunnel.hengda.cloudns.biz#05-godlike_tunnel-ua-tr',    
}
for vps_name,str in dict.items():
    print('vps_name=',vps_name,',str=',str)
    text=str.split('#')[0]             # 去掉节点名称（#及后面内容）
    num=text.find('@')
    str_0=text[:num+1]
    print('str_0=',str_0)

    str_1=text[num+1:]
    num=str_1.find('?')
    ip=str_1[:num].split(':')[0]           # 取得ip
    print('ip=',ip)

    domains.append(ip)                      # 添加自己节点的IP到domains
    str_1=str_1[num+1:]
    num=str_1.find('&')
    str_1=str_1[num+1:]                   # 取得节点剩余字符
    print('str_1',str_1)

    filepath = f'../{vps_name}.txt'   # 文件路径
    print('file path:',filepath,',file is exist:',os.path.exists(filepath))

    if os.path.exists(filepath):            # 如果存在节点文件则删除
        os.remove(filepath)
    with open(filepath, 'a') as f:
        for domain in domains:
            print('domain=',domain)
            for port in port_tuple_01:
                coment=vps_name+'_'+domain.split('.')[0]+':'+port
                txt = str_0  + domain + ':' + port + '?security=tls&' + str_1 + '#'+coment
                print('txt=',txt)
                f.write(txt + '\n')
            for port in port_tuple_02:
                coment = vps_name + '_' + domain.split('.')[0]+':'+port
                txt = str_0 + domain + ':' + port + '?security=none&' + str_1 + '#'+coment
                f.write(txt + '\n')



