Summary:	Tools for the NILFS filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików NILFS
Name:		nilfs-utils
Version:	2.2.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.nilfs.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	57480da0c9e6c35100e157b6cc87b6f8
URL:		http://www.nilfs.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libmount-devel
BuildRequires:	libuuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NILFS is a log-structured file system supporting versioning of the
entire file system and continuous snapshotting which allows users to
even restore files mistakenly overwritten or destroyed just a few
seconds ago.

This package provides utilities for NILFS.

%description -l pl.UTF-8
NILFS to system plików o strukturze logu, obsługujący wersjonowanie
całego systemu plików i ciągłe migawki, co pozwala użytkownikom
odtwarzać nawet pliki przez pomyłkę nadpisane lub zniszczone kilka
sekund wcześniej.

Ten pakiet dostarcza narzędzia do systemu plików NILFS.

%package devel
Summary:	Header files for NILFS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki NILFS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libuuid-devel

%description devel
Header files for NILFS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki NILFS.

%package static
Summary:	Static NILFS library
Summary(pl.UTF-8):	Statyczna biblioteka NILFS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static NILFS library.

%description static -l pl.UTF-8
Statyczna biblioteka NILFS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-libmount
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
%doc AUTHORS ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nilfs_cleanerd.conf
%attr(755,root,root) /sbin/mkfs.nilfs2
%attr(755,root,root) /sbin/mount.nilfs2
%attr(755,root,root) /sbin/nilfs-clean
%attr(755,root,root) /sbin/nilfs-resize
%attr(755,root,root) /sbin/nilfs-tune
%attr(755,root,root) /sbin/nilfs_cleanerd
%attr(755,root,root) /sbin/umount.nilfs2
%attr(755,root,root) %{_bindir}/chcp
%attr(755,root,root) %{_bindir}/dumpseg
%attr(755,root,root) %{_bindir}/lscp
%attr(755,root,root) %{_bindir}/lssu
%attr(755,root,root) %{_bindir}/mkcp
%attr(755,root,root) %{_bindir}/rmcp
%attr(755,root,root) %{_libdir}/libnilfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnilfs.so.0
%attr(755,root,root) %{_libdir}/libnilfscleaner.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnilfscleaner.so.0
%attr(755,root,root) %{_libdir}/libnilfsgc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnilfsgc.so.0
%{_mandir}/man1/lscp.1*
%{_mandir}/man1/lssu.1*
%{_mandir}/man5/nilfs_cleanerd.conf.5*
%{_mandir}/man8/chcp.8*
%{_mandir}/man8/dumpseg.8*
%{_mandir}/man8/mkcp.8*
%{_mandir}/man8/mkfs.nilfs2.8*
%{_mandir}/man8/mount.nilfs2.8*
%{_mandir}/man8/nilfs.8*
%{_mandir}/man8/nilfs-clean.8*
%{_mandir}/man8/nilfs-resize.8*
%{_mandir}/man8/nilfs-tune.8*
%{_mandir}/man8/nilfs_cleanerd.8*
%{_mandir}/man8/rmcp.8*
%{_mandir}/man8/umount.nilfs2.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnilfs.so
%attr(755,root,root) %{_libdir}/libnilfscleaner.so
%attr(755,root,root) %{_libdir}/libnilfsgc.so
%{_libdir}/libnilfs.la
%{_libdir}/libnilfscleaner.la
%{_libdir}/libnilfsgc.la
%{_includedir}/nilfs*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libnilfs.a
%{_libdir}/libnilfscleaner.a
%{_libdir}/libnilfsgc.a
