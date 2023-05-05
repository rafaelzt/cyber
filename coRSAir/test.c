#include <stdio.h>
#include <assert.h>
#include <openssl/bn.h>

#define MAXLEN 500

int main(int argc, char *argv[])
{
    size_t len;
    unsigned char in[MAXLEN];
    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *x = BN_new();
    BIGNUM *r = BN_new();

    if (argc != 2) {
	printf("no file given\n");
	return -1;
    }
    FILE *f = fopen(argv[1], "rb");
    if (!f) {
	printf("can't open file\n");
	return -1;
    }

    len = fread(in, sizeof(char), MAXLEN, f);
    fclose(f);


    BN_bin2bn(in, len, x);

    BN_sqr(r, x, ctx);
    BN_mul(x, x, x, ctx);

    BN_print_fp(stdout, r);
    printf("\n");
    BN_print_fp(stdout, x);
    printf("\n");

    assert(BN_cmp(r, x) == 0);

    BN_free(x);
    BN_free(r);
    BN_CTX_free(ctx);

    return 0;

}
