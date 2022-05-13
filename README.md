# Generate random password & password hash

Generate a password hash from user input, or generate a random password and its
hash and show both on the output.

## Usage

```yaml
      - uses: licenseware/generate-password-hash@v1
        name: Get password hash
        id: passwd-hasher
        with:
          password: change-this-or-dont-even-provide-one
          length: 16
```

## Inputs

| Name | Description | Required | Default |
|------|-------------|----------|---------|
| password | The password you want to hash | false | `<generated>` |
| length | The length of the password hash | false | 16 |

## Outputs

| Name | Description | Example |
|------|-------------|---------|
| password | The password printed again | false | a-secure-password |
| password-hash | The hash of the password | false | hashed-value |
