Name:    buxton
Version: 2
Release: 1
License: LGPL-2.1
Group:   Framework/system
Summary: buxton
Source0: %{name}-%{version}.tar.bz2
Source1001: %{name}.manifest

BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(libsystemd-daemon)
BuildRequires: gdbm-devel
BuildRequires: libattr-devel
Requires: %{name}-libs = %{version}-%{release}
Requires: gdbm

%description
buxton

%package libs
Summary:  buxton libraries
License:  LGPL-2.1

%description libs
buxton devel

%package devel
Summary:  buxton devel
License:  LGPL-2.1
Requires: %{name} = %{version}-%{release}

%description devel
buxton devel

%prep
%setup -q

%build
cp %{SOURCE1001} .
./autogen.sh --with-user=root --disable-manpages
make %{?_smp_mflags}

%install
%make_install

# Make sure this directory exist
mkdir -p %{buildroot}%{_sharedstatedir}/buxton

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
cat LICENSE.LGPL2.1 > $RPM_BUILD_ROOT%{_datadir}/license/buxton
cat LICENSE.LGPL2.1 > $RPM_BUILD_ROOT%{_datadir}/license/buxton-libs

%post
mkdir -p %{_sysconfdir}/systemd/default-extra-dependencies/ignore-units.d
ln -s %{_libdir}/systemd/system/buxton.service %{_sysconfdir}/systemd/default-extra-dependencies/ignore-units.d/

%files
%defattr(-,root,root,-)
%{_datadir}/license/buxton
%dir %{_sharedstatedir}/buxton
%{_sysconfdir}/buxton.conf
%{_bindir}/buxtonctl
%{_libdir}/systemd/system/buxton.service
%{_libdir}/systemd/system/buxton.socket
%{_libdir}/systemd/system/sockets.target.wants/buxton.socket
%{_sbindir}/buxtond
%manifest %{name}.manifest

%files libs
%defattr(-,root,root,-)
%{_datadir}/license/buxton-libs
%{_libdir}/libbuxton.so.*
%{_libdir}/buxton/gdbm.so
%{_libdir}/buxton/memory.so
%manifest %{name}.manifest

%files devel
%defattr(-,root,root,-)
%{_includedir}/buxton.h
%{_libdir}/libbuxton.so
%{_libdir}/pkgconfig/libbuxton.pc
%manifest %{name}.manifest
