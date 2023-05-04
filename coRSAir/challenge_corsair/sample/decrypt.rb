require 'openssl'
key = OpenSSL::PKey::RSA.new File.read 'private.pem'
print key.private_decrypt File.read 'message.bin'
