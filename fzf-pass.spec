Name:           fzf-pass
Version:        0.1
Release:        1%{?dist}
Summary:        A posix script that helps you find Youtube videos (with out API) and opens/downloads using mpv/youtube-dl.
License:        GPLv3
Url:            https://github.com/FunctionalHacker/fzf-pass
Source0:        https://github.com/FunctionalHacker/fzf-pass/archive/refs/tags/v%{version}.tar.gz

Requires:       fzf
Requires:       pass
Requires:       ydotool

%description

This is a script heavily inspired by rofi-pass, but with FZF instead of Rofi. There's still a lot to do and this is just the first version. As it is now, it is only compatible with Sway


%prep
%autosetup -n %{name}-%{version}


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Mar 30 2021 Ben Homan <ben@benhoman.com>
- Initial RPM Release
