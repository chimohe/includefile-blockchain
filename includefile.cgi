use Crypt::Digest::SHA256 qw(sha256_hex);
use Crypt::RSA;
use Crypt::RSA::Key;

sub includefile {
    my $fname = shift;
    my @_array = @_;

    # Remove potentially harmful characters from the file name
    $fname =~ s/([\&;\`'\|\"*\?\~\^\(\)\[\]\{\}\$\n\r])//g;

    # Open the file for appending
    if (!open(INCLUDE, '>>', $fname)) {
        return '[an error occurred while processing this directive]';
    }

    # Generate a private key for signing
    my $private_key = Crypt::RSA::Key::Private->generate( Size => 1024 );
    my $public_key = $private_key->public_key();

    # Append the @_array data, signatures, and proof-of-work to the file
    my $target_zeros = 4;  # The required number of leading zeros in the hash
    my $nonce = 0;
    foreach my $item (@_array) {
        my $signature = $private_key->sign_string($item, 'SHA-256');

        # PoW: Find the correct nonce value
        my $data_with_nonce = "$item:$signature:$nonce";
        my $hash = sha256_hex($data_with_nonce);
        while (substr($hash, 0, $target_zeros) ne "0" x $target_zeros) {
            $nonce++;
            $data_with_nonce = "$item:$signature:$nonce";
            $hash = sha256_hex($data_with_nonce);
        }

        print INCLUDE "$data_with_nonce\n";
    }

    # Close the file
    close(INCLUDE);

    return 1;  # Indicate success
}

# Example usage
my $filename = "blockchain.txt";  # Replace with the desired file name
my @data_to_append = ("Block 1 data", "Block 2 data", "Block 3 data");

# Append the @_array, signatures, and PoW to the file for blockchain
my $result = includefile($filename, @data_to_append);
if ($result) {
    print "Data successfully added to the blockchain file.\n";
} else {
    print "Error adding data to the blockchain file.\n";
}
