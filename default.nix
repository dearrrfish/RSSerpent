with import <nixpkgs> {};

let
    pythonPackages = python310Packages;
in pkgs.mkShell rec {
    name = "python-shell";

    venvDir = "./.venv";

    buildInputs = [
        pythonPackages.python
        poetry
    ];

    shellHook = ''
      export PATH="$HOME/.detaspace/bin:$PATH"
      export LD_LIBRARY_PATH=${stdenv.cc.cc.lib}/lib/
    '';

}
