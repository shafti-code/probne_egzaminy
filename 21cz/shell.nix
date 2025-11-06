{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.clang-tools
    pkgs.zig
    pkgs.python3
    pkgs.python3Packages.pyqt6
  ];

  shellHook = ''
  echo "welcome, player one"
  echo "i loaded:
pkgs.clang-tools
pkgs.zig
python3
python3Packages.pyqt6
  "
  '';
}

