#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	CSV parser and writer library
Summary(pl.UTF-8):	Biblioteka do analizy i zapisu danych CSV
Name:		libcsv
Version:	3.0.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libcsv/%{name}-%{version}.tar.gz
# Source0-md5:	d3307a7bd41d417da798cd80c80aa42a
URL:		https://sourceforge.net/projects/libcsv/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CSV library provides a flexible, intuitive interface for parsing
and writing CSV data. 

%description -l pl.UTF-8
Biblioteka CSV zapewnia elastyczny, intuicyjny interfejs do analizy i
zapisu danych CSV.

%package devel
Summary:	Header file for libcsv library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libcsv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libcsv library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libcsv.

%package static
Summary:	Static libcsv library
Summary(pl.UTF-8):	Statyczna biblioteka libcsv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcsv library.

%description static -l pl.UTF-8
Statyczna biblioteka libcsv.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcsv.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libcsv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcsv.so.3

%files devel
%defattr(644,root,root,755)
%doc FAQ 
%attr(755,root,root) %{_libdir}/libcsv.so
%{_includedir}/csv.h
%{_mandir}/man3/csv.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcsv.a
%endif
