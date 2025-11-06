{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.mono
  ];

  shellHook = ''
  echo "why are we still here?
  just to suffer ?"
  '';
}


