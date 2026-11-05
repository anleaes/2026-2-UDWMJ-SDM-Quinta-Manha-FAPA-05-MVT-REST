{
    description = "Car Rental Django App";

    inputs = {
        nixpkgs.url = "nixpkgs/nixos-unstable";
    };

    outputs =
        { self, nixpkgs }:
        let
            system = "x86_64-linux";
            pkgs   = import nixpkgs {
                inherit system;

                config.allowUnfreePredicate = pkg:
                builtins.elem (nixpkgs.lib.getName pkg) [
                    "sqlcl"
                ];
            };
        in
        {
            devShells.${system}.default = pkgs.mkShell {
                buildInputs = with pkgs; [
                    sqlcl
                    pyright
                    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
                        python-decouple
                        pillow
                        markdown
                        oracledb
                        django-widget-tweaks
                        django-filter
                        django-stubs
                    ]))
                ];
            };
        };
}
