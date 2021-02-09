#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define PUBLICEXPONENT 65537

typedef struct pub_key{
    uint64_t n ;
    uint32_t e ;
} pub_key_t;

typedef struct pri_key{
    uint64_t n ;
    uint64_t d ;
} pri_key_t;

typedef struct rsa_keys {
    pub_key_t pubkey;
    pri_key_t selfkey;
}rsa_keys_t;

rsa_keys_t my_rsa_keys = {.pubkey.e = PUBLICEXPONENT,};

/*
扩展欧几里的算法
计算 ax + by = 1中的x与y的整数解（a与b互质）
a,b ∈ Z
必存在整數 x,y 使ax+by = gcd(a,b)
ret: gcd(x,y)
*/
int exgcd(uint64_t a,uint64_t b,int64_t *x,int64_t *y)
{
    int ret  ,t ;
    if(b==0)
    {
        *x=1;
        *y=0;
        return a;
    }
    ret=exgcd(b,a%b,x,y);
    t=*x;
    *x=*y;
    *y=t-a/b*(*y);
    return ret;
}

long long binpow(long long a, long long b, long long m) {
  a %= m;
  long long res = 1;
  while (b > 0) {
    if (b & 1) res = res * a % m;
    a = a * a % m;
    b >>= 1;
  }
  return res;
}

/*
# 生成公钥私钥，p、q为两个超大质数
def gen_key(p, q):
    n = p * q
    fy = (p - 1) * (q - 1)      # 计算与n互质的整数个数 欧拉函数
    e = 65537                    # 选取e   一般选取65537
    # generate d
    a = e
    b = fy
    r, x, y = ext_gcd(a, b)
    # 计算出的x不能是负数，如果是负数，说明p、q、e选取失败，不过可以把x加上fy，使x为正数，才能计算。
    if x < 0:
        x = x + fy
    d = x
    # 返回：   公钥     私钥
    return    (n, e), (n, d)

*/

int gen_key(uint64_t p, uint64_t q){
    uint64_t n = p * q;
    uint64_t fy = (p - 1) * (q - 1) ;
    uint64_t e = PUBLICEXPONENT;
    //generate d
    uint64_t a = e;
    uint64_t b = fy ;
    int64_t x , y;
    printf("debug: a:%lu , b:%lu\n",a,b);
    int r = exgcd(a,b,&x,&y);
    if(x < 0){
        printf("warning , x < 0\n");
        x = x + fy ;
    }
    printf("x:%ld , y:%ld \n",x,y);
    uint64_t d = x;

    my_rsa_keys.pubkey.n= n ;
    my_rsa_keys.selfkey.n = n ;
    my_rsa_keys.selfkey.d = d ;
    return 0;
}


uint64_t decrypt(uint64_t m, pri_key_t prikey){
    return binpow(m, prikey.d, prikey.n);
}

uint64_t encrypt(uint64_t c, pub_key_t pubkey){
    return binpow(c,pubkey.e,pubkey.n);
}

int main(int argc , char* argv[]){
    uint64_t p = 10091 , q = 1033;

    gen_key(p,q);
    printf("p:%lu , q:%lu \n",p,q );
    printf("e:%u\n",my_rsa_keys.pubkey.e);
    printf("n:%lu\n",my_rsa_keys.pubkey.n);
    printf("d:%lu\n",my_rsa_keys.selfkey.d);

    uint64_t m = 4410967;
    printf("ori : %lu\n",m);
    /*
    uint64_t c = encrypt(m,my_rsa_keys.selfkey);
    printf("encrypted : %llu\n",c);
    printf("decrypted : %llu\n",decrypt(c,my_rsa_keys.pubkey));
    */
    uint64_t c = encrypt(m,my_rsa_keys.pubkey);
    printf("encrypted : %lu\n",c);
    printf("decrypted : %lu\n",decrypt(c,my_rsa_keys.selfkey));

}