{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
  ];

  shellHook = ''
  echo "hello shafti... remember c will always be better"
  '';
}

