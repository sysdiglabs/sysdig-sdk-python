{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default =
          with pkgs;
          mkShell {
            packages = [
              python310 # Minimum supported python version in this project
              uv
              ruff
              pre-commit

              # LSPs
              python3Packages.python-lsp-server
              basedpyright
            ];

            shellHook = ''
              pre-commit install
            '';
          };

        formatter = pkgs.nixfmt-rfc-style;
      }
    );
}
