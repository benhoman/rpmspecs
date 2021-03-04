%define version 0.1.0
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%define reponame ytfzf

Name:           ytfzf
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A posix script that helps you find Youtube videos (with out API) and opens/downloads using mpv/youtube-dl.
License:        GPLv3
Url:            https://github.com/pystardust/ytfzf
Source0:        https://github.com/pystardust/ytfzf/archive/master.tar.gz

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
%autosetup -n %{reponame}-master


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Mar 04 2021 Ben Homan <ben@benhoman.com>
- 
