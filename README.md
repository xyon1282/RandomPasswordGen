# RandomPasswordGen

This program is a random password generator, used to generate random passwords with the makeup chosen by the users terminal commands. The default configuration will be to create a password with the common requirements for most websites. eg : (A special character, at least one number, a capital letter, and 8 characters in length)

-----------------------------------------

## Download/Installation

```powershell
git clone https://github.com/xyon1282/RandomPasswordGen.git
```

```powershell
cd RandomPasswordGen
```

## Usage

```python
python password.py
```

This command above will create a password with the default/expected makeup for most websites today (A special character, at least one number, a capital letter, and 8 characters in length)

In order to change the makeup of the password you would use --num, --spec, --up, and --low flags. Ill provide an example below:

```powershell
python password.py --num 3 --spec 2 --up 1 --low 2
```

The above command will produce an 8 character password with 3 numbers, 2 special characters, 1 uppercase letter and 2 lowercase ones. Example output below:

```powershell
y52Lv9!^
```