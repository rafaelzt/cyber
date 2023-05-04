#include <openssl/pem.h>
#include <openssl/rsa.h>
#include <openssl/bio.h>
#include <stdio.h>

int main() {
    const char *public_key_file = "public.pem";

    // Leer la clave pública RSA desde el archivo
    FILE *file = fopen(public_key_file, "r");
    if (file == NULL) {
        perror("Error al abrir el archivo de clave pública");
        return 1;
    }

    EVP_PKEY *evp_pkey = PEM_read_PUBKEY(file, NULL, NULL, NULL);
    fclose(file);

    if (evp_pkey == NULL) {
        printf("Error al leer la clave pública RSA\n");
        return 1;
    }

    RSA *rsa_key = EVP_PKEY_get1_RSA(evp_pkey);

    // Imprimir detalles de la clave pública RSA
    BIO *bio = BIO_new(BIO_s_mem());
    RSA_print(bio, rsa_key, 0);

    // Leer e imprimir el contenido del BIO
    char *bio_content;
    long bio_length = BIO_get_mem_data(bio, &bio_content);
    fwrite(bio_content, 1, bio_length, stdout);

    // Liberar recursos
    BIO_free(bio);
    RSA_free(rsa_key);
    EVP_PKEY_free(evp_pkey);

    return 0;
}

