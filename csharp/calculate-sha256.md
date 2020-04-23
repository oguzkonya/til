# Calculate SHA256

Calculating SHA256 hash of a string is fairly easy:

    public static string SHA256(string input)
    {
        var bytes = System.Text.Encoding.UTF8.GetBytes(input);

        using (var hash = System.Security.Cryptography.SHA256.Create())
        {
            var hashedInputBytes = hash.ComputeHash(bytes);
            var hashedInputStringBuilder = new System.Text.StringBuilder(64);

            for (int i = 0; i < hashedInputBytes.Length; i++)
            {
                hashedInputStringBuilder.Append(hashedInputBytes[i].ToString("X2"));
            }

            return hashedInputStringBuilder.ToString();
        }
    }

You can replace SHA256 with SHA512 if you need a stronger encryption, but if you do that you'd also need to replace StringBuilder(64) with StringBuilder(128), because the output would be 128 bytes long instead of 64.