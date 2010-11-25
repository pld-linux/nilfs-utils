Summary:	Tools for the NILFS filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików NILFS
Name:		nilfs-utils
Version:	2.0.20
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.nilfs.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	04287d6c96df7d823a096c203021a2ec
URL:		http://www.nilfs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NILFS is a log-structured file system supporting versioning of the
entire file system and continuous snapshotting which allows users to
even restore files mistakenly overwritten or destroyed just a few
seconds ago.

This package provides utilities for NILFS.

%package devel
Summary:	Header files for NILFS
Summary(pl.UTF-8):	Pliki nagłówkowe NILFS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for NILFS.

%description devel -l pl.UTF-8
Pliki nagłówkowe NILFS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/nilfs_cleanerd.conf
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.so.0
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
