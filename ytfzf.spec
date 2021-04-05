%define version 1.1.2
%define reponame ytfzf

Name:           ytfzf
Version:        %{version}
Release:        1%{?dist}
Summary:        A posix script that helps you find Youtube videos (with out API) and opens/downloads using mpv/youtube-dl.
License:        GPLv3
Url:            https://github.com/pystardust/ytfzf
Source0:        https://github.com/pystardust/ytfzf/archive/refs/tags/v%{version}.tar.gz

Requires:       mpv
Requires:       youtube-dl
Requires:       jq
Recommends:       fzf

%description

A posix script that helps you find Youtube videos (with out API) and opens/downloads using mpv/youtube-dl.
    * Thumbnails
    * History support
    * Download support
    * Format selection (and default formats)
    * Queue multiple tracks (using fzf multiselection)


%prep
%autosetup -n %{reponame}-%{version}


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Apr 05 2021 Ben Homan <ben@benhoman.com>
- Updated version to 1.1.2

* Tue Mar 30 2021 Ben Homan <ben@benhoman.com>
- Modified Version numbers to follow github release tags.

* Thu Mar 04 2021 Ben Homan <ben@benhoman.com>
- Initial RPM Release
