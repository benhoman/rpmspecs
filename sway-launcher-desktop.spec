%define version 0.1.0
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%define reponame sway-launcher-desktop

Name:           sway-launcher-desktop
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        TUI-based launcher menu made with bash and the amazing fzf.
License:        GPLv3
URL:            https://github.com/Biont/sway-launcher-desktop
Source0:        https://github.com/Biont/sway-launcher-desktop/archive/master.tar.gz
Requires:       fzf

%description

This is a TUI-based launcher menu made with bash and the amazing fzf. Despite its name, it does not (read: no longer) depend on the Sway window manager in any way and can be used with just about any WM.
Features
    * Lists and executes available binaries
    * Lists and executes .desktop files (entries as well as actions)
    * Does not depend on xdg-utils. Just pure bash and awk
    * Shows a preview window containing whatis info of binaries and the Comment= section of .desktop files
    * History support which will highlight recently used entries
    * Colored output and glyphs for the different entry types
    * Entries are lazily piped into fzf eliminating any lag during startup
    * Optional support for the XDG Autostart specification
    * Executes arbitrary custom commands (if there are no other matches)


%prep
%autosetup -n %{reponame}-master


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name}.sh %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE
%{_bindir}/%{name}


%changelog
* Thu Mar 04 2021 Ben Homan <ben@benhoman.com>
- 
